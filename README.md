<div align="center">
  <img src="https://media.giphy.com/media/L2kr3y97uJauF6T6Lh/giphy.gif" width="100"/>
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>GlowBeyond(Ecommerce Application)</h1>

<h4>A Full stack ecommerce application made using Vue.JS for frontend and Django Rest Framework for backend. The application is coupled with [auth-application](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application) for login and jwt token authentication.</h4>


 Main Features</h2>

* Feature to list all the latest products on the home page
* Categories of summer and winter are available. Products are classified based on these categories
* A product details page with all the information about the product with the feature of adding the product to cart along with the quantity specified
* A cart page with all the products along with their quantity added in the cart listed in tabular form. The quantity can be increased or decreased  and the products can be deleted/removed from the cart directly from the table.
* Proper error handling
* Proper error and success notifications
* Jwt token authentication using the authentication application linked in the description. 
* An account details page with the user information, available user coupons and the user orders.
* The application uses mysql as the database

#




### Technologies used

<div style="display:flex">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
<img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
 
![Quasar](https://img.shields.io/badge/Quasar-16B7FB?style=for-the-badge&logo=quasar&logoColor=black)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  
</div>

#
<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>


![home](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/053b6fef-5bc7-4265-b40b-64692c669863)
![home2](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/e8b5214d-046d-4d40-a10a-540aed073210)
![summer](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/74228fea-72ab-49ac-889c-7f0220d6c4a8)
![winter](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/1faeb934-24ad-4a08-83f4-ccae3a0ffd65)
![proddetails](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/9bb3277c-b1b4-48c2-ac7d-dd25d0f31873)
![cart](https://github.com/Abdul-Mueed-Shahbaz/Eccomerce-Application/assets/52679916/f77a13fe-fc09-4900-b01d-406c1832ca83)
hAuthApplication](https://user-images.githubusercontent.com/52679916/207143548-6a925a9f-e4a6-4082-ba18-09d1a3e98fbc.png)
![Cart](https://user-images.githubusercontent.com/52679916/207143476-2587bc15-ccf9-40b7-be99-d04647310322.png)
![Checkout](https://user-images.githubusercontent.com/52679916/207143485-048a50e6-ddf4-48d7-b57c-c49ff39ea3a5.png)

<h2><img width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0134.gif" border="0" alt="animated-television-image-0134" />

### How to add products
* There is no role based views feature available yet. So the only way to add the products is using django-admin
#


<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Commands:</h2>

##
Install the dependencies
(FrontEnd/gui)
```bash
yarn
# or
npm install
```
(BackEnd/api)
```
# Create virtual env by executing the setup.bat in the build folder
# Activate the venv by using the activate file in the build-env/scripts folder
# After completing the above mentioned steps
# Install the required packages by executing the following command
pip install -r .\requirements\bast.txt 
# Change the settings file if you want to change the database related information
# Use the manage.py file and execute the following commands to apply required migrations
python manage.py makemigrations 
python manage.py migrate
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```
### To start the server
```
python manage.py runserver 8000
```

### Lint the files
```bash
yarn lint
# or
npm run lint
```



### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).

