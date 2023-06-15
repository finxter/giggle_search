from .models import Joke


def test_data_generator(amount):
    for i in range(0, amount):
        new_joke_object = Joke(
            query = "zombie watermelons",
            response = "Why did the zombie watermelon break up with his girlfriend? Because he thought she was a little too rotten!"
        )
        new_joke_object.save()