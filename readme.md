# open the cmd


## cd management_proj

## env/Scripts/activate


# pip install -r requirements.txt


# python manage.py runserver

-- Initial
   $ go mod init

-- start the process
   $ go run .

-- open postman setup POST method paste below url - $ http://localhost:8080/post_json
-- Click on the "Body" section.
-- Choose the "Raw" format option.
-- Change the "Type" to JSON and paste given input JSON like below.

{
"ev": "top_cta_clicked",
"et": "clicked",
"id": "cl_app_id_001",
"uid": "cl_app_id_001-uid-001",
"mid": "cl_app_id_001-uid-001",
"t": "Vegefoods - Free Bootstrap 4 Template by Colorlib",
"p": "http://shielded-eyrie-45679.herokuapp.com/contact-us",
"l": "en-US",
"sc": "1920 x 1080",
"atrk1": "button_text",
"atrv1": "Free trial",
"atrt1": "string",
"atrk2": "color_variation",
"atrv2": "ESK0023",
"atrt2": "string",
"atrk3": "page_path",
"atrv3": "/blog/category_one/blog_name.html",
"atrt3": "string",
"atrk4": "source",
"atrv4": "facebook",
"atrt4": "string",
"uatrk1": "user_score",
"uatrv1": "1034",
"uatrt1": "number",
"uatrk2": "gender",
"uatrv2": "m",
"uatrt2": "string",
"uatrk3": "tracking_code",
"uatrv3": "POSERK093",
"uatrt3": "string",
"uatrk4": "phone",
"uatrv4": "9034432423",
"uatrt4": "number",
"uatrk5": "coupon_clicked",
"uatrv5": "true",
"uatrt5": "boolean",
"uatrk6": "opt_out",
"uatrv6": "false",
"uatrt6": "boolean"
}




