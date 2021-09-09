from dataclasses import dataclass

@dataclass
class Person:
    """[summary]

    Returns:
        [type]: [description]
    """    """[summary]

    Returns:
        [type]: [description]
    """
    name : str
    description :str = ''

    def saluda(self, other_person):
        """Method to communicate with

        Args:
            otra_persona ([Person]): [Person to communicate with]

        Returns:
            [string]: [message]
        """
        return f'Hola "{other_person.name}" me llamo "{self.name}"'
