University Name: http://www.sjsu.edu/<br>
Course: Cloud Technologies (CMPE281) <br>
Professor: Sanjay Garje <br>
Student: 
- Sangwon Song (LinkedIn: https://www.linkedin.com/in/sangwon-song-5a7384b2/)
- Han-Wei Lin (LinkedIn: https://www.linkedin.com/in/han-wei-lin-9b55a1142/)

Demo: https://youtu.be/eJEt0gP7uBY

Project Introduction (What the application does, feature list) <br>
Our project idea was that historical pictures taken before color cameras were invented have grayscale image values. To help people investigate and analyze the information of the gray-scaled images more accurately, colorizing the pictures will be necessary and useful.
Our application implements colorizing gray-scaled photos and to detect object labels in the photos to be used to do a simple search using the label. 
![Project Architecture](https://drive.google.com/uc?export=view&id=1XS-t4MzhrGwyGM34txlQt1IML_9vBoBx)
Sample Demo Screenshots
* Project Main Page
![](https://drive.google.com/uc?export=view&id=1betF4ybXFJxCu7L6t7hXTlFlBpbu8AOf)
![](https://drive.google.com/uc?export=view&id=1YGF81ARUK_QPtp6x0w9phmR1x5e8BzX5)
* Test Images
![](https://drive.google.com/uc?export=view&id=1EuGdQY9o51RRCXYd4lvkThG-LV02QDBP)
![](https://drive.google.com/uc?export=view&id=1Q7toA8vwAaWeI-_TDutOssqK0QG_I5nn)

Pre-requisites Set Up

AWS Services needed:
- CodePipeline
- S3
- EC2 - ELB - AutoScaling
- RDS - MySQL
- R53
- CloudFront
- Lambda
- Rekognition

In the EC2 or local machine:
- Follow https://pypi.org/project/mysqlclient/ to install mysqlclient library for python.
- git clone https://github.com/Wayne122/ColorMe_CMPE281_Project2.git
- pip install -r requirements.txt
- replace all the config in project1/settings.py with your AWS API Key also the Google and Facebook API Key optionally
