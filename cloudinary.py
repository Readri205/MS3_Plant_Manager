import os
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Cloudinary settings using python code. Run before pycloudinary is used.
cloudinary.config(
  cloud_name=os.environ.get('cloud_name'),
  api_key=os.environ.get('api_key'),
  api_secret=os.environ.get('api_secret')
)


# Cloudinary API call details
cloudinary_cloud_name = os.environ.get('cloud_name')
cloudinary_api_key = os.environ.get('api_key')
cloudinary_api_secret = os.environ.get('api_secret')


# @app.route("/upload_cloudinary_images")
# def upload_cloudinary_images():
#    cloudinary.uploader.upload("", width=200, height=400,
#                               crop="fill", gravity="face")


# upload_cloudinary_images()


@app.route("/cloudinary_images")
def cloudinary_images():
    data = cloudinary.Search()\
        .expression('mygardenmanager')\
        .max_results('30')\
        .with_field('tags')\
        .execute()
    images = data["resources"]
#    for k in images:
#        version = k['version']
#        filename = k['filename']
#        print(version, filename)
#    print(json.dumps(images, indent=2))
    for tags in images:
        tag = tags['tags']
#        for i in tag:
#            print(i)
#        print(tag)
#    print(json.dumps(images, indent=2))
    return render_template(
        "my_images.html", data=data,
        images=images, tag=tag)

# cloudinary_images()


@app.route("/cloudinary_search")
def cloudinary_search():
    data = cloudinary.Search()\
        .expression('folder:mygardenmanager')\
        .max_results('30')\
        .with_field('tags')\
        .execute()
    images = data["resources"]
    for tags in images:
        tag = tags['tags']
        print(tag)
    print(json.dumps(tags, indent=2))
#    print(url)
#    with open(url, "rb") as file:
#        txt_image = [base64.b64encode(file.read()).decode("ascii")]
#        print(txt_image)


# cloudinary_search()


@app.route("/cloudinary_resources")
def cloudinary_resources():
    data = cloudinary.api.resources(
        max_results='100',
        resource_type='image',
        type='upload',
        prefix='mygardenmanager/')
    images = data["resources"]
    print(json.dumps(images, indent=2))
#    return render_template(
#        "my_images.html", data=data, images=images)


# cloudinary_resources()


# @app.route("/cloudinary_update")
def cloudinary_update():
    data = cloudinary.api.update(
        'mygardenmanager/Sunflower',
        tags='Flower, Yellow',
        created_by='ricardo2')
    print(json.dumps(data, indent=2))


# cloudinary_update()


@app.route("/cloudinary_rename")
def cloudinary_rename():
    cloudinary.uploader.rename(
        'mygardenmanager/vvshquurn8x9bqlmfibr',
        'mygardenmanager/Contemplation')
#    print(json.dumps(data, indent=2))


# cloudinary_rename()


@app.route("/cloudinary_delete")
def cloudinary_delete():
    data = cloudinary.api.delete_resources('')
    print(json.dumps(data, indent=2))


# cloudinary_delete()


@app.route("/cloudinary_destroy")
def cloudinary_destroy():
    public_id = request.args.get('public_id', type=str)
    params = str(public_id)
    cloudinary.uploader.destroy(params)
#    print(result)
    return redirect(url_for(
        "cloudinary_images"))


# cloudinary_destroy()

# def get_image(url, file_path, file_name):

# with urllib.request.urlopen(
# 'https://bs.floristic.org/
# image/o/1a03948baf0300da25558c2448f086d39b41ca30') as response:
#     url = response.read()

