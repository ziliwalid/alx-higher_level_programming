#!/usr/bin/python3
import json
import turtle
import csv

"""defining base model"""
class Base:
    """describes the base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """intits a new base
        Args:
            id (int): new base's id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
     def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of items.
        Args:
            list_dictionaries (list):list of items
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps([item.to_dictionary() for item in list_dictionaries])

    @classmethod
      def save_to_file(cls, list_objs):
        """serialises JSON
        Args:
            list_objs (list): list instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if li is None:
                jsonfile.write("[]")
            else:
                list_dicts = [instance.to_dictionary() for instance in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """deserialises a JSON string
        Args:
            js (str): js param
        Returns:
            deserialises a JSON string
        """
        if js is None or js == "[]":
            return []
        return [cls.create(**d) for d in json.loads(json_string)]

    @classmethod
    def create(cls, **dictionary):
        """Return a class from a dictionary
        Args:
            **dictionary (dict): dictionary param
        """
        if dictionary and dictionary != {}:
            new_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """return  list of classes from a JSON
        Returns:
            list of classes from a JSON
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return list_dicts
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """returns the CSV serialization of a list of instances to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for instance in list_objs:
                    writer.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """return a list of classes from a CSV file
        Returns:
             a list of classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares :)
        Args:
            list_rectangles (list): list of rectangles param
            list_squares (list): list of squares param
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")

        for rect in lr:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in ls:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

