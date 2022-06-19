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

create table dillercenter(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
address TEXT NOT NULL
)


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
image TEXT NOT NULL,
FOREIGN KEY(equipmentid) REFERENCES equipment(id),
FOREIGN KEY(enginetypeid) REFERENCES enginetype(id),
FOREIGN KEY(gearboxtypeid) REFERENCES gearboxtype(id),
FOREIGN KEY(cartypeid) REFERENCES cartype(id),
FOREIGN KEY(firmid) REFERENCES firm(id)
);


create table dillercentercar(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
carid INTEGER NOT NULL,
dillercenterid NOT NULL
)


create table testdrives(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
autoid INTEGER NOT NULL,
dillercenterid INTEGER NOT NULL,
testdrivedate  UNSIGNED BIG INT NOT NULL,
clientid INTEGER NOT NULL,
status BOOLEAN DEFAULT FALSE,
FOREIGN KEY(autoid) REFERENCES auto(id),
FOREIGN KEY(clientid) REFERENCES client(id),
FOREIGN KEY(dillercenterid) REFERENCES dillercenter(id)
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

INSERT INTO auto(produceyear,equipmentid, enginetypeid, gearboxtypeid, cartypeid, firmid,model, enginevolume, horsepower,baterycapacity, image  ) VALUES
(2020, 3, 2, 2, 5, 3, '911 Turbo S', 4.3, 850, null, 'https://www.nicepng.com/png/detail/237-2375010_911-turbo-s-porsche-models.png'),
(2018, 1, 1, 2, 1, 2, 'Model S', null, 945, 67.9, 'https://www.kindpng.com/picc/m/125-1250076_transparent-tesla-png-tesla-model-s-transparent-png.png'),
(2022, 2, 2, 2, 4, 1, 'Transporter', 5.2, 230, null, 'https://ukr-prokat.com/wp-content/uploads/2018/09/T6.jpg'),
(2020, 4, 2, 2, 3, 5, 'C4', 1.2, 125, null,  'https://www.seekpng.com/png/small/367-3678493_new-c4-cactus-citroen-c4.png'),
(2020, 2, 3, 2, 5, 4, 'Tundra TRD Pro', 5.7, 675, null,'https://www.kindpng.com/picc/m/615-6158151_toyota-tundra-trd-pro-19-hd-png-download.png'),
(2020, 2, 2, 1, 5, 4, 'Tundra TRD Pro', 5.3, 601, null,'https://www.pngkey.com/png/detail/394-3945360_new-2018-toyota-tundra-platinum-2019-tundra-trd.png' );


INSERT INTO dillercenter(name, address) VALUES
("Toyota Center", "м.Харків, вул.Сумська, 90"),
("Elite cars showroom", "м.Київ, вул.Хрещатик, 17"),
("Every day cars", "м.Харків, пр.Героїв Харкова, 327"),
("Citroen center", "м.Львів, вул.Героїв України, 25");

INSERT INTO dillercentercar(carid, dillercenterid) VALUES
(1, 2),
(1, 2),
(3, 3),
(4, 3),
(4, 4),
(5, 1),
(5, 3),
(6, 1);






