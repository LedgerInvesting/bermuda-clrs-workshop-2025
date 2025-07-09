# Bermuda Workshop CLRS 2025

Instructions here detail the steps necessary to set up your machine for the Bermuda Python package workshop. With proper installation, you will be able to run all the workshop scripts, notebooks, and related examples discussed throughout the workshop. Participants may be on any of MacOS, Windows, or Linux operating systems. Most of these operating systems will come with a pre-installed version of Python, but for the workshop you may need to install a more recent version, as discussed further below.

The general steps are:

1. Install Python 3.10 or higher
2. Create a Python virtual environment 
3. Activate the Python virtual environment
4. Install necessary Python packages, including Bermuda
5. Verify installation
6. Create and link Jupyter kernel

## 1. Install Python 3.10 or higher 

Go to https://www.python.org/downloads/ and download a version of Python that is at minimum version 3.10.1. If you already have an existing Python installation that meets this criteria, you can skip this step. 

## 2. Create a Python virtual environment

Navigate to your local version of the workshop directory in your terminal (macOS or Linux) or PowerShell (Windows):

  ### MacOS/Linux

  ```
  cd path/to/materials
  ```

  ### PowerShell

  ```
  cd C:\path\to\materials
  ```

Next, create a virtual environment named env: 

  ### MacOS/Linux/PowerShell

  ```
  python -m venv env
  ```

## 3. Activate the virtual environment

You can then activate the virtual environment per: 

  ### MacOS/Linux

  ```
  source env/bin/activate
  ```

  ### PowerShell

  ```
  .\env\Scripts\Activate
  ```


## 4. Install necessary Python packages

Finally, install the necessary Python requirements, all of which can be found in the requirements/requirements.txt file. They can all be installed with the one-liner: 

  ### MacOS/Linux

  ```
  pip install -r requirements/requirements.txt
  ```

  ### PowerShell

  ```
  pip install -r requirements\requirements.txt
  ```

## 5. Verify installation

To verify that installation was successful, kick off python and try importing bermuda:

  ### MacOS/Linux/Windows

  ```
  python
  import bermuda as tri
  ```

Next, while still in the Python interpreter, import the test data and try creating a simple triangle plot: 

  ### MacOS/Linux/Windows

  ```
  from bermuda import meyers_tri
  meyers_tri.plot_data_completeness().show()
  ```

## 6. Create and link Jupyter kernel

We will use Jupyter notebooks to interactively work through the various different bermuda features, use-cases, and exercises. All the necessary requirements are already installed per step 4, but a Jupyter kernel needs to be created and linked to the virtual environment from step 2. To do so, starting from the activated virtual environment (i.e. after step 3), run the following: 

  ### MacOS/Linux/PowerShell

  `python -m ipykernel install --user --name=env --display-name bermuda-clrs-2025`

Once the kernel is installed and linked, you can open a Jupyter notebook either in your favorite IDE or in the browser per: 
		
  ### MacOS/Linux/PowerShell

  `jupyter notebook`

Once the notebook is live, select the bermuda-clrs-2025 kernel, and you will now have a notebook available with all the workshop requirements installed. Note that we will work through the notebooks in the GitHub repository linked at the top of this document. When opening each notebook for the first time, you will need to select the bermuda-clrs-2025 kernel so that requirements are available. 
