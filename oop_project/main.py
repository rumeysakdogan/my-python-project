from user import User
from post import Post

app_user_one = User("rr@dd.com", "Rumeysa Dogan", "pwd1", "Cloud engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("tets@test.com", "James Bond", "supersecret", "Agent" )
app_user_two.get_user_info()

post_one = Post("I love Python!", app_user_one.name)
post_one.get_post_info()