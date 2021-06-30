# Spritesheet Splitter
## A python script that can split pre-existing spritesheets into a bunch of png images using its XML

<div>requires:  
    <ul>
        <li><a href="https://www.python.org">python</a> (with pip included)</li>
        <li>Pillow <code>pip install Pillow</code></li>
        <li>Your spritesheet and your XML files (both in one folder with nothing other than these files and the python script inside that folder)</li>
    </ul>
</div>
<p>Usage: Inside the folder where you have the script, spritesheet and XML, goto the naviagation bar (the one that has your folder name), type <code>cmd</code> (for windows) and press enter. Make sure the folder with your spritesheet and XML doesn't have anything else in it as this program is gonna generate a lot of files in that folder.</p>
<p>Now type in <code>python SpriteSplitter.py &lt;Your spritesheet's name&gt;</code></p>
<p>This will generate a bunch of pngs according to the XML file</p>
<p>Note: This can generate some duplicates if some frames were re-used inside the xml, so just manually delete those.</p>