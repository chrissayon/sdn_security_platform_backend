The purpose of this project was to create a SDN security system. The project is supposed to be deployed together with the backend repository of this project at https://github.com/chrissayon/sdn_security_platform_frontend, and the whole automated deployment of this project on the cloud can be found at https://github.com/chrissayon/sdn_security_platform_provision.

How this project functions: Provided you already know about SDN architecture, the backend of this project periodically pings a OpenFlow controller and gets statistics from the exposed controller API. It takes this data and performs so calculations to get periodic/incremental data and also runs the data through a machine learning model to check for DDoS attacks. It also runs the data through a machine learning model which was developed using TensorFlow 2.0 in python which will give a probability of whether the network is being attacked or not (though as byte count is the metric then this means that the scale of the network needs to be taken into account on whether the network is being attacked).

Backend Information:
If you want to see this website working in full functionality then install and run the frontend and backend on the same host; or you could alternatively run the frontend on the EC2 instance which would try to ping the backend on your local computer which you're accessing the browser from. 

The provisioning repository is able to deploy both the code to both frontend and backend on seperate hosts, but with the way the code is designed you won't get the full functionality if you run them on seperate hosts. The SDN Security Platform provision is more of a way for to demonstrate my DevOps skills and I was using this project as a means to do that.

Setup: Assuming you have python already installed, go into the root directory and install all the dependancies (best to do this inside a virtual environment)
#### pip install -r requirements.txt

Afterwards, you can start the server by running:
#### python manage.py runserver
