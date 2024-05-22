MikroTik Hotspot auto login
===========================

This project automates the login process for the school WiFi using MikroTik Hotspot and designed for Sochcollege of IT ,Pokhara Nepal,But can be customized to your flavour of choice.


Setup Instructions
------------------

Follow these steps to set up and run the project:

1. **Set Up Virtual Environment**:

   It's recommended to use a virtual environment to manage your project dependencies. Set up and activate a virtual environment using the following commands:

   .. code-block:: bash

      python -m venv .venv
      # On Windows
      .\.venv\Scripts\activate
      # On Linux/MacOS
      source .venv/bin/activate


2. **Install Python Dependencies**:

   Make sure you have Python and pip installed. Install the required Python packages using:

   .. code-block:: bash

      pip install -r requirements.txt


3. **Install Express.js**:

   Ensure you have Node.js installed. Install Express.js using npm:

   .. code-block:: bash

      npm install express

4. **Run the Project**:

   Use the provided Makefile to run the project. The `make run` command will start the necessary services and scripts:

   .. code-block:: bash

      make run

   This will:
   
   - Start the Express Js server listening for requests to be handeled for md5 hashing.
   - Activate the Python virtual environment and run the necessary Python scripts.


5. **Note**
    MakeFile is not currently Supported in windows you can run 

   .. code-block:: bash

      node md5.js # on one terminal 
      python connect.py # on other terminal with virtualenv activated
    
6. **LICENSE**
   GNU General Public License v3.0
