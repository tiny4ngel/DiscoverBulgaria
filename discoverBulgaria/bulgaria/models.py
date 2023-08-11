from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Landmarks(models.Model):
    """
        Model representing a landmark.

        Attributes:
            title (CharField): The title of the landmark.
            location (CharField): The location of the landmark.
            landmark_photo (CloudinaryField): The photo of the landmark.
            trip_time (CharField): The trip time for visiting the landmark.
            historic_context (CharField): The historic context of the landmark.
            architectural_features (CharField): The architectural features of the landmark.
            visitor_information (CharField): Information for visitors to the landmark.
            accessibility (CharField): Accessibility information for the landmark.
            cover_photo (CloudinaryField): The cover photo of the landmark.
            additional_photo (CloudinaryField): Additional photo of the landmark.

        Methods:
            __str__: Returns a string representation of the landmark (title).
        """
    title = models.CharField(max_length=100, )
    location = models.CharField(max_length=100, )
    landmark_photo = CloudinaryField('landmark photo', null=True, blank=True)
    trip_time = models.CharField(max_length=100, )
    historic_context = models.CharField(max_length=1000)
    architectural_features = models.CharField(max_length=1000)
    visitor_information = models.CharField(max_length=1000)
    accessibility = models.CharField(max_length=1000)
    cover_photo = CloudinaryField('cover photo', null=True, blank=True)
    additional_photo = CloudinaryField('additional photo', null=True, blank=True)

    def __str__(self):
        return self.title


class FavouriteLandmarks(models.Model):
    """
        Model representing a user's favorite landmark.

        Attributes:
            traveller (ForeignKey): The user who marked the landmark as a favorite.
            landmark (ForeignKey): The landmark that is marked as a favorite.

        Meta:
            unique_together: Ensures that each user can only mark a landmark as a favorite once.
    """
    traveller = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    landmark = models.ForeignKey(Landmarks, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        unique_together = ['traveller', 'landmark']


class HistoricFigure(models.Model):
    """
        Model representing a historic figure.

        Attributes:
            name (CharField): The name of the historic figure.
            lifespan (CharField): The lifespan of the historic figure.
            biography (TextField): The biography of the historic figure.
            figure_photo (CloudinaryField): The photo of the historic figure.
            additional_photo (CloudinaryField): Additional photo of the historic figure.
            quote (TextField): A notable quote from the historic figure.
            unlocked_by (ManyToManyField): Users who unlocked this historic figure.

        Methods:
            __str__: Returns a string representation of the historic figure (name).
    """
    name = models.CharField(max_length=100)
    lifespan = models.CharField(max_length=100)
    biography = models.TextField()
    figure_photo = CloudinaryField('figure_photo', null=True, blank=True)
    additional_photo = CloudinaryField('additional photo', null=True, blank=True)
    quote = models.TextField()
    unlocked_by = models.ManyToManyField(UserModel, blank=True)

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    """
        Model representing a user's leaderboard position.

        Attributes:
            user (OneToOneField): The user associated with the leaderboard position.
            points (IntegerField): The points earned by the user.
    """
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField(default=0)


class QuizQuestion(models.Model):
    """
        Model representing a quiz question related to a historic figure.

        Attributes:
            historic_figure (ForeignKey): The historic figure associated with the quiz question.
            question_text (CharField): The text of the quiz question.

        Methods:
            __str__: Returns a string representation of the quiz question.
    """
    historic_figure = models.ForeignKey(HistoricFigure, on_delete=models.CASCADE, related_name='quiz_questions')
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
        Model representing a choice for a quiz question.

        Attributes:
            question (ForeignKey): The quiz question associated with the choice.
            choice_text (CharField): The text of the choice.
            is_correct (BooleanField): Indicates if the choice is the correct answer.
    """
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

