def htmlhelp():
  return """<html>
    <body>
    <h2>Script Runner Help</h2>
    <br>
    <i>Run it like you own it</i>

    <p>
    <a href="#design">Design Options</a><br>
    <a href="#requirements">Requirements for Your Script</a><br>
    <a href="#working_with_scripts">Working with Scripts</a><br>
    </p>
    <a name="design"/>
    <p>
    The Script Runner allows you to execute a script in QGIS to automate
    a task. The script can use two approaches to access the QGIS API:
    </p>
    <ol>
    <li>Use the qgis.utils.iface object</li>
    <li>Import qgis.core and qgis.gui</li>
    </ol>
    <p>
    In the first method, you are limited to to only those methods supported
    by the QgisInterface class. In the second you have full access to the PyQGIS API.
    </p>
    <a name="requirements"/>
    <h4>Requirements</h4>
    <p>
    In order for Script Runner to execute your script you must define a
    <em>run_script</em> function that accepts a single argument. This is the standard
    entry point used by Script Runner. A reference to
    the qgis.utils.iface object will be passed to your <em>run_script</em> function.
    You don't have to use the iface object in your script but your
    <em>run_script</em> function must accept it as an argument.  
    </p>
   <p>
   Here is an example of a simple <em>run_script</em> function:
   </p>
   <pre>
    def run_script(iface):
        ldr = Loader(iface)
        ldr.load_shapefiles('/vmap0_shapefiles')
    </pre>
   
   <p>
   In this example, the <em>run_script</em> creates an instance (ldr) of a class named
   Loader that is defined in the same source file. It then calls a method in the Loader
   class named load_shapefiles to do something useful---in this case, load all the
   shapefiles in a specified directory.
   </p>
   <p>
   Alternatively, you could choose not to use classes and just do everything
   within the <em>run_script</em> function, including having it call functions
   in the same script or others you might import. The important thing is to be sure
   you have defined a <em>run_script</em> function. If not, Script Runner won't load
   your script.
   </p>
   <h4>Working with Scripts</h4>
   <p>
   To run a script, you must add it to Script Runner using the <em>Add Script</em> tool on the toolbar. This will add it to a list in the left panel. This list of scripts is persisted between uses of QGIS. You can remove a script using the <em>Remove Script</em> tool. This just removes it from the list; it does nothing to the script file on disk.
   </p>
   <p>
   Once you have a script loaded, you can click the <em>Script Info</em> tool
   to populate the Info and Source tabs in the panel on the right. The Info tab
   contains the docstring from your module and then a list of the classes,
   methods, and functions found in the script. Having a proper docstring at the
   head of your script will help you determine the puprose of script.  </p>
   <p> 
   You can view the source of the script on the Source tab. This allows you
   to quickly confirm that you are using the right script and it does what you
   think it will.
   </p>
   
    </body>
    </html>"""
