import sqlalchemy
import flask
import json


from sqlalchemy.ext.declarative import declarative_base

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])


def index():
    # Define the MariaDB engine using MariaDB Connector/Python
    engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:Password123!@172.75.0.3/company")

    Base = declarative_base()

    class Employee(Base):
        __tablename__ = 'employees'
        id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
        firstname = sqlalchemy.Column(sqlalchemy.String(length=100))
        lastname = sqlalchemy.Column(sqlalchemy.String(length=100))
        active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    Base.metadata.create_all(engine)

    # Create a session
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    def addEmployee(firstName,lastName):
         newEmployee = Employee(firstname=firstName, lastname=lastName)
         session.add(newEmployee)
         session.commit()

    def selectAll():
        employees = session.query(Employee).all()
        output=""
        for employee in employees:
           output += (" - " + employee.firstname + ' ' + employee.lastname)
        return output




    # Show all employees

    names = selectAll()
    output = ('\n\nFrom Mariadb:\nAll Employees ' + names + '\n' + 'Project by Wyatt LeMaster wwl0004 \n\n')
    return output




app.run(debug=True, port=8080, host='0.0.0.0')
