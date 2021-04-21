import os
import json
from random import choice, randint
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from data.model import UserProfile, db, connect_to_db
from crud import *
from datetime import datetime


def create(
    email,
    password,
    first_name,
    last_name,
    insta_handle,
    bio,
    post_title,
    post_description,
    makeup_type,
    posts,
    profile_picture,
    products=[],
):
    u = create_user(email=email, password=password)
    u.userprofiles.append(
        UserProfile(
            user_id=u.user_id,
            first_name=first_name,
            last_name=last_name,
            insta_handle=insta_handle,
            bio=bio,
            profile_picture=profile_picture,
        )
    )
    for post in posts:
        p = Post(
            user_id=u.user_id,
            title=post_title,
            post_description=post_description,
            makeup_type=makeup_type,
        )
        for post_image in post:
            p.makeupimages.append(MakeupImage(image=post_image))

        p.products.append(
            Product(
                title="Foundation",
                details="Nars Longwear",
                url="https://www.sephora.com/",
                image="1.png",
            )
        )
        u.posts.append(p)
        db.session.commit()

    # for product in products:
    #     create_postproducts(product.product_id, o.post_id)
    return u


def add_sample_data():

    users_list = []
    profiles_list = []
    posts_list = []
    favorites_list = []
    products_list = []

    # Product 1
    p = create_product(
        "Foundation",
        "Nars Longwear",
        "https://www.sephora.com/",
        "1.png",
    )
    products_list.append(p)

    # Product 2
    p = create_product(
        "Concealer",
        "Huda Beauty Concealer for Dark Skin",
        "https://www.sephora.com/",
        "2.png",
    )
    products_list.append(p)

    # Product 3
    p = create_product(
        "Concealer",
        "Huda Beauty Concealer For Light Skin",
        "https://www.sephora.com/",
        "3.png",
    )
    products_list.append(p)

    # Product 4
    p = create_product(
        "Concealer",
        "Huda Beauty makeup brushes",
        "https://www.sephora.com/",
        "1.png",
    )
    products_list.append(p)

    u = create(
        email="amanda@outlook.com",
        password="123",
        first_name="Amanda",
        last_name="Cerney",
        insta_handle="@madihagoheerofficial",
        bio="Some test bio",
        post_title="Dramatic makeup",
        post_description="This is a look that I created using these products",
        makeup_type="Dramatic",
        posts=[
            ["1_0.jpg", "1_1.jpg", "1_2.jpg"],
            ["6_0.jpg", "6_1.jpg", "6_2.jpg"],
            ["7_0.jpg", "7_1.jpg", "7_2.jpg"],
            ],
        profile_picture="1.jpg",
        products=products_list,
    )
    users_list.append(u)

    u = create(
        email="huda@outlook.com",
        password="123",
        first_name="madiha",
        last_name="Latif",
        insta_handle="@madihagoheerofficial",
        bio="Some test bio",
        post_title="Dramatic makeup",
        post_description="This is a look that I created using these products",
        makeup_type="Dramatic",
        posts=[
            ["2_0.jpg", "2_1.jpg", "2_2.jpg"],
            ["8_0.jpg", "8_1.jpg", "8_2.jpg", "8_3.jpg"],
            ["9_0.jpg","9_1.jpg",]
        ],
        profile_picture="2.jpg",
        products=products_list,
    )
    users_list.append(u)

    u = create(
        email="madihagoheer@outlook.com",
        password="123",
        first_name="Madiha",
        last_name="Goheer",
        insta_handle="@madihagoheerofficial",
        bio="Some test bio",
        post_title="Dramatic makeup",
        post_description="This is a look that I created using these products",
        makeup_type="Dramatic",
        posts=[
            ["3_0.jpg"],
            ["10_0.jpg", "10_1.jpg",]
        ],
        profile_picture="3.jpg",
        products=products_list,
    )
    users_list.append(u)

    u = create(
        email="myreengoheer@outlook.com",
        password="123",
        first_name="Myreen",
        last_name="Goheer",
        insta_handle="@madihagoheerofficial",
        bio="Some test bio",
        post_title="Dramatic makeup",
        post_description="This is a look that I created using these products",
        makeup_type="Dramatic",
        posts=[
            ["4_0.jpg"],
            [ "11_0.jpg", "11_1.jpg"],
            ["12_0.jpg","12_1.jpg"]
        ],
        profile_picture="1.jpg",
        products=products_list,
    )
    users_list.append(u)

    create_comment(1, 1, "This is a commnet on post 1")
    create_comment(1, 2, "This is a commnet on post 2")
    create_comment(1, 3, "This is a commnet on post 3")
    create_comment(1, 4, "This is a commnet on post 4")
    create_comment(2, 4, "This is a commnet on post 4")
    create_comment(3, 4, "This is a commnet on post 4")
    create_comment(4, 4, "This is a commnet on post 4")

    db.session.add_all(profiles_list)
    db.session.commit()

    print("Added objects to DB")


def add_sample_images():
    os.system("cp -r data/sampledata/* static/images/")


if __name__ == "__main__":
    from flask import Flask

    os.system("rm -r static/images/profile/*.jpg")
    os.system("rm -r static/images/products/*")
    os.system("rm -r static/images/posts/*.jpg")
    os.system("dropdb finalproject")
    os.system("createdb finalproject")

    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()
    add_sample_data()
    add_sample_images()
