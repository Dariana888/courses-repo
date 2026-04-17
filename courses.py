from fastapi import FastAPI

app = FastAPI()

COURSES = [
    Courses(id: 1,
            title: "Mathematics",
            trainer: "John Smith",
            description: "Fundamentals of math",
            duration_weeks: 4
),
    Courses(id: 2,
            title: "Computer Science",
            trainer: "Marry Poppins",
            description: "Fundamentals of computer science",
            duration_weeks: 8
),
    Courses(id: 3,
            title: "Java Backend",
            trainer: "Martin Morgan",
            description: "OOP, variables and loops",
            duration_weeks: 3
),
    Courses(id: 4,
            title: "Python",
            trainer: "Andrew Louder",
            description: "Python & Python Pro",
            duration_weeks: 5
),
  Courses(id: 5,
            title: "Databases",
            trainer: "Mark Michigan",
            description: "Lorem ipsum description",
            duration_weeks: 20
),

@app.get("/courses")
async def read_all_courses():
    return COURSES


class Course:
    id:             int
    title:          str
    trainer:        str
    description:    str
    duration_weeks: int
    def __init__(self, id, title, trainer, description, duration_weeks):
        self.id             = id
        self.title          = title
        self.trainer        = trainer
        self.description    = description
        self.duration_weeks = duration_weeks