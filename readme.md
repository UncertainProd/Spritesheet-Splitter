# Spritesheet Splitter
## A quick little python script that can split pre-existing spritesheets into a bunch of png images using its XML

<div>requires:  
    <ul>
        <li><a href="https://www.python.org">python</a> (with pip included)</li>
        <li>Pillow <code>pip install Pillow</code></li>
        <li>Your spritesheet and your XML files (both in one folder with nothing other than these files and the python script inside that folder)</li>
    </ul>
</div>
<p>Usage: Inside the folder where you have the script, spritesheet and XML, goto the naviagation bar (the one that has your folder name), type <code>cmd</code> (for windows) and press enter. Make sure the folder with your spritesheet and XML doesn't have anything else in it as this program is gonna generate a lot of files in that folder.</p>
<p>Now type in <code>python SpriteSplitter.py &lt;Your spritesheet's name&gt; &lt;Base-name for all output files&gt;</code></p>
<p>This will generate a bunch of pngs according to the XML file. If the base-name is provided (say it's "sample") all files will be named <code>sample-##.png</code> (# = a digit) else by default it uses the pose-name from the xml to name the files.</p>
<p>Sidenote: If the base-name contains a space (eg: mommy mearest) the it must be typed within quotes (like this: "mommy mearest").</p>
<p>Note: This can generate some duplicates if some frames were re-used inside the xml, so just manually delete those.</p>