from users.shemas import CreateUser


async def create_user(user_new: CreateUser):
    user = user_new.model_dump()
    return {
        'user': user
    }