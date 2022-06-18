create table equipment(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

create table enginetype(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

create table gearbox(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

create table cartype(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

create table firm(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);


create table client(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
login TEXT NOT NULL,
password TEXT NOT NULL,
registrationdate UNSIGNED BIG INT DEFAULT ( CAST(strftime('%s', 'now') AS UNSIGNED BIG INT))
);


create table auto(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
produceyear  INTEGER NOT NULL,
equipmentid INTEGER NOT NULl,
enginetypeid INTEGER NOT NULL,
gearboxtypeid INTEGER NOT NULL,
enginevolume DOUBLE,
cartypeid INTEGER NOT NULL,
firmid INTEGER NOT NULL,
model TEXT NOT NULL,
horsepower DOUBLE NOT NULL,
baterycapacity DOUBLE,
FOREIGN KEY(equipmentid) REFERENCES equipment(id),
FOREIGN KEY(enginetypeid) REFERENCES enginetype(id),
FOREIGN KEY(gearboxtypeid) REFERENCES gearboxtype(id),
FOREIGN KEY(cartypeid) REFERENCES cartype(id),
FOREIGN KEY(firmid) REFERENCES firm(id)
);


create table testdrives(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
autoid INTEGER NOT NULL,
testdrivedate  UNSIGNED BIG INT NOT NULL,
clientid INTEGER NOT NULL,
FOREIGN KEY(autoid) REFERENCES auto(id),
FOREIGN KEY(clientid) REFERENCES client(id)
);


INSERT INTO equipment(name) VALUES
("luxury"),
("standart"),
("sport"),
("citymobile");

INSERT INTO enginetype(name) VALUES
("electrical"),
("gas"),
("diesel");

INSERT INTO gearbox(name) VALUES
("mechanical"),
("automation");

INSERT INTO cartype(name) VALUES
("sedan"),
("hatchback"),
("suv"),
("van"),
("sport car"),
("truck");

INSERT INTO firm(name) VALUES
("VolksWagen"),
("Tesla"),
("Porsche"),
("Toyota"),
("Citroen");

INSERT INTO client(login, password) VALUES 
("test1", "123123"),
("test2", "123123"),
("test", "123123");

INSERT INTO auto(produceyear,equipmentid, enginetypeid, gearboxtypeid, cartypeid, firmid,model, enginevolume, horsepower,baterycapacity  ) VALUES
(2020, 3, 2, 2, 5, 3, '911 Turbo S', 4.3, 850, null ),
(2018, 1, 1, 2, 1, 2, 'Model S', null, 945, 67.9),
(2022, 2, 2, 2, 4, 1, 'Transporter', 5.2, 230, null ),
(2020, 4, 2, 2, 3, 5, 'C4', 1.2, 125, null ),
(2020, 2, 3, 2, 5, 4, 'Tundra TRD Pro', 5.7, 675, null ),
(2020, 2, 2, 1, 5, 4, 'Tundra TRD Pro', 5.3, 601, null );






