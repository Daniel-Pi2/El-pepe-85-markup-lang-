# import os
import re
# import subprocess as sp


def main()->None:

    global is_block
    is_block = False

    global is_body
    is_body = False

    global is_numbered
    is_numbered = False

    global block_lines
    block_lines = 0

    written_lines=[]


    try:

        filename = input("file to read: \n")
        output_filename = input("file to write: \n")

        with open(filename, "r") as f:

            i = 0
			

            for line in f.readlines():

                if i == 0:

                    written_lines.append("<html>\n")
                
                line = interpreter(line)

                written_lines.append(line)	
                
                i+=1

            written_lines.append("\n</html>")


        print(f"{filename} has been read. {i} lines.")

        with open(output_filename, "w") as o:
            
            o.writelines(written_lines)



    except Exception as e:
        print(f"Oops!\n{e}")

def interpreter(line:str)->str:

    global is_body

    left_body = re.compile(r"^\:\:[body]")
    right_body = re.compile(r"[body]\:\:")

    left = len(re.findall(left_body, line))>=1
    right = len(re.findall(right_body, line))>=1

    print(line)

    if len(line) >= 2:

        if left and "|" not in line:
            is_body = True
            line = line.replace("::body","<body>")
        elif right and "|" not in line:
            line = line.replace("body::", "</body>")
            is_body = False
            
        else:

            if is_body:
                line = formatting(line)
            else:
                line = line

        return line

    else:
        if is_block:
            return block(line)
        else:
            return ""

def block(line:str)->str:

    global is_block

    global is_numbered

    global block_lines

    multiline = re.compile(r"^[|]")

    is_multiline = len(re.findall(multiline, line)) >= 1

    if ("==pre" in line) or ("==code" in line) or ("==par" in line) : # BEGIN BLOCK

        block_lines=0

        is_block = True

        if "==pre" in line: # begin pre
            
            block_lines += 1
            line = line.replace("==pre","<pre>")
        elif "==code" in line: #begin code

            block_lines += 1

            if ":" in line:
                
                code_class = line.split(":")[1]

                if "numberLines" in code_class:
                    is_numbered = True
                else:
                    is_numbered = False

                if len(line.split(":"))>=3:

                    start = line.split("==code")[1].split(":")[2]

                    try:
                        block_lines = int(start)
                    except:
                        block_lines = 1

                    try:
                        
                        topic = line.split("==code")[1].split(":")[3]

                        if "\n" in topic:

                            topic = topic.replace("\n","")

                        title = "users/you@123 % " + topic + " @ " + code_class.split(" ")[0]
                    except:
                        title = "users/you@123 % " + code_class.split(" ")[0]

                    line = f"<div class=\"code\"><pre class=\"{code_class}\" startFrom=\"{start}\"><code>\n" + title + "\n" + 30*"*" + "\n"

                else:
                    line = f"<div class=\"code\"><pre class=\"{code_class}\"><code>" + "\nusers/you@123 %\n" + code_class + 30*"*" + "\n"
            else:
                 line = f"<pre><code>"

        elif "==par" in line: #begin p block

            block_lines += 1

            #########################################
            def par_classify(classes:list[str], content:str)->str:

                try:

                    for element in classes:

                        if element in content: # our prioritizd classes are gonna be put on top

                            try:
                                extra_class = content.replace(element, "")
                                return element + " " + extra_class
                            
                            except: # some class python couldn't parse, it's a safe output mode

                                return element 
                        else: 
                            pass
                    else:   
                        try:
                            return content
                        except Exception as e:
                            print(e)
                            return "left"

                except Exception as e:

                    print(e)

                    return "left"
            ###########################################

            if ":" in line:

                par_class = line.split(":")[1]
                hierarchy = ["justify","right","center","left"]

                try: # Heading for the classy p block
                    title = "<b>" + line.split(":")[2] + "</b>"

                    par_class = par_classify(hierarchy, par_class)

                    line = "<p class=\"" + par_class + "\" >" + title

                except:

                    par_class = par_classify(hierarchy, par_class)

                    line = "<p class=\"" + par_class + "\" >"

                finally:

                    if "numberLines" in par_class:
                        is_numbered = True
                    


        return line

    elif ("pre==" in line) or ("code==" in line) or ("par==" in line): #END BLOCK

        is_numbered = False

        is_block = False

        if "pre==" in line:
            
            block_lines = 0
            line = line.replace("pre==", "</pre>")
        
        elif "code==" in line:

            block_lines = 0
            line = line.replace("code==", "</code></pre></div>")

        elif "par==" in line:

            line = line.replace("par==", "</p>")
        
        return line

    elif is_multiline or is_block: #INSIDE A BLOCK  

        block_lines += 1

        if is_multiline: #MULTILINE FORMAT OVERRIDES BLOCK FORMAT

            if is_numbered:

                return line.replace("|", f"[{block_lines-1}]")

            else:
            
                return line.replace("|", f"<!--{block_lines-1}-->")
        
        if is_block:

            if is_numbered:

                return f"[{block_lines-1}] " + line
            
            else:

                return f"<!--{block_lines-1}-->" + line


    # Default

    else:
        return "<p> " + line + " </p>"


def formatting(text:str)->str:

    # Markdown Headings


    level_1 = re.compile(r"^\#{1}")
	
    level_2 = re.compile(r"^\#{2}")
	
    level_3 = re.compile(r"^\#{3}")
	
    level_4 = re.compile(r"^\#{4}")
	
    level_5 = re.compile(r"^\#{5}")

    level_6 = re.compile(r"^\#{6}")

	# text.split(re.findall(level_1,text)[0])[1]

    if len(re.findall(level_6,text)) > 0:

        text = text.split(re.findall(level_6,text)[0])[1]
        text = "<h6 id=\"heading\">" + text + " </h6>"



    elif len(re.findall(level_5,text)) > 0:

        text = text.split(re.findall(level_5,text)[0])[1]
        text = "<h5 id=\"heading\">" + text + " </h5>"


    elif len(re.findall(level_4,text)) > 0:

        text = text.split(re.findall(level_4,text)[0])[1]
        text = "<h4 id=\"heading\">" + text + " </h4>"



    elif len(re.findall(level_3,text)) > 0:

        text = text.split(re.findall(level_3,text)[0])[1]
        text = "<h3 id=\"heading\">" + text + " </h3>"


    elif len(re.findall(level_2,text)) > 0:

        text = text.split(re.findall(level_2,text)[0])[1]
        text = "<h2 id=\"heading\">" + text + " </h2>"



    elif len(re.findall(level_1,text)) > 0:

        text = text.split(re.findall(level_1,text)[0])[1]
        text = "<h1 id=\"heading\">" + text + " </h1>"
		
    else: # Zim Styled Headings

        def is_heading(beg,end, content:str)->bool: #zim wiki inspired heading notation accepted folks!!!

            left = len(re.findall(beg,content))>0
            right = len(re.findall(end,content))>0

            if left and right:
                return True
            else:
                return False


        left1 = re.compile(r"^[=]{6}")
        right1 = re.compile(r"[=]{6}$")

        left2 = re.compile(r"^[=]{5}")
        right2 = re.compile(r"[=]{5}$")

        left3 = re.compile(r"^[=]{4}")
        right3 = re.compile(r"[=]{4}$")

        left4 = re.compile(r"^[=]{3}")
        right4 = re.compile(r"[=]{3}$")

        left5 = re.compile(r"^[=]{2}")
        right5 = re.compile(r"[=]{2}$")

        left6 = re.compile(r"^[=]{1}")
        right6 = re.compile(r"[=]{1}$")

        if is_heading(left1, right1, text):

            text = text.replace("======"," ")
            text = "<h1 id=\"heading\">" + text + "</h1>"

        elif is_heading(left2, right2, text):

            text = text.replace("====="," ")
            text = "<h2 id=\"heading\">" + text + "</h2>"

        elif is_heading(left3, right3, text):

            text = text.replace("===="," ")
            text = "<h3 id=\"heading\">" + text + "</h3>"

        elif is_heading(left4, right4, text):

            text = text.replace("==="," ")
            text = "<h4 id=\"heading\">" + text + "</h4>"

        elif is_heading(left5, right5, text):

            text = text.replace("=="," ")
            text = "<h5 id=\"heading\">" + text + "</h5>"

        elif is_heading(left6, right6, text):

            text = text.replace("="," ")
            text = "<h6 id=\"heading\">" + text + "</h6>"

        else: # Final Block Evaluation
             
            text = block(text)


    return text



main()
