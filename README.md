
# Capstone Project: Structures Crack Detection

This project uses a mordified Xception Keras application to detect crack in structures. The model is currently trained on more than 20000+ images of cracks in concrete structures and no cracks in concrete.
The model returns a value between one and zero. The closer to one the value, the higher the accuracy of an actual crack being detected. Hence, values greater than  0.5 or equal to one means a crack has been detected. A value less than 0.5 means no crack was detected in the image. This was implemented in the juypter notebook.  
 

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Authors

- Abdul-Rashid Zakaria (Zak)

Github: https://github.com/ZachJon1

You can also connect with me on twitter and linkedin

twitter: https://twitter.com/AbdulRashidZak2

linkedin: https://www.linkedin.com/in/abdul-rashid-zakaria-eit-001/



## Demo

Check the folder screenshots for images of demo run locally, and using AWS Lambda and API gateway


## Deployment

For local deployment, follow the following steps:

Download all the files from capstone_project

Open the Lambda_function file

Open this webpage: https://github.com/ZachJon1/capstone_project/blob/main/img/test_1.jpg

Click on download and  Copy the web address

Paste the copied webaddress into the Lambda_function url line (This step is necessary to test model with data, you can use another image of your choosing. Two images are provided in the img folder)

Save the lambda_function file with Ctrl + S keyboard shortcut or any other way of your choice

Open a windows terminal, an Ubuntu terminal tab was used in running all the code.

cd into the directory with all the files downloaded from capstone_project

run to build docker file

$ docker build -t model_x .

Next thing is to run 

$ docker run --rm -p 8080:8080 model_x

Open another Ubuntu terminal tab or use visual studio 

run 

$ python test.py

Congrats you have run the model locally.



AWS Lambda and API gateway was used in the web services deployment. 

Requirements: 

Access to AWS

Preinstalled AWS command line interface

Push docker image to AWS ECR


For an easy walkthrough on deploying this model on AWS watch these videos:

https://www.youtube.com/watch?v=kBch5oD5BkY&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=97

https://www.youtube.com/watch?v=wyZ9aqQOXvs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=98



