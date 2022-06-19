import React, {useEffect, useState} from 'react';
import {
    Box,
    CircularProgress,
    FormControl,
    IconButton,
    InputLabel,
    MenuItem,
    Select,
    Slider, Tooltip,
    Typography
} from "@mui/material";
import {Api} from "../../api/Api";
import DriveEtaIcon from '@mui/icons-material/DriveEta';
import InfoIcon from '@mui/icons-material/Info';
import cl from './Catalog.module.css';
import ModalCar from "./components/ModalCar";
import ModalTestDrive from "./components/ModalTestDrive";

const Catalog = () => {

    const [loading, setLoading] = useState(false)
    const [cars, setCars] = useState([]);

    const [categories, setCategories] = useState([]);
    const [category, setCategory] = useState("Оберіть тип кузову");

    const [engineTypes, setEngineTypes] = useState([]);
    const [engineType, setEngineType] = useState("Оберіть тип двигуна");

    const [firm, setFirm] = useState("Оберіть виробника");
    const [model, setModel] = useState(null);
    const [fuel, setFuel] = useState([]);
    const [firms, setFirms] = useState([]);

    const [yearRange, setYearRange] = useState([2000, 2022])
    const [engineRange, setEngineRange] = useState([1.0, 6.0])
    const [enginePRange, setEnginePRange] = useState([100, 1000])

    const [modal, setModal] = useState(false);
    const [modalTest, setModalTest] = useState(false);
    const [currentCar, setCurrentCar] = useState(-1);

    useEffect(() => {
        const api = new Api();
        try {
            setLoading(true);
            const promises = [];

            const promise1 = new Promise((resolve, reject) => {
                api.getCars().then(res => {
                    const firms = new Array(...new Set(res.data.cars.map(r => r.firm)));
                    const categories = new Array(...new Set(res.data.cars.map(r => r.car_type)));
                    const enginies = new Array(...new Set(res.data.cars.map(r => r.engine)));
                    setFirms(["Оберіть виробника", ...firms]);
                    setCategories(["Оберіть тип кузову", ...categories]);
                    setEngineTypes(["Оберіть тип двигуна", ...enginies]);
                    setCars([...res.data.cars]);
                    resolve(true);
                }).catch(err => {
                    reject(err);
                });
            })

            promises.push(promise1);

            Promise.all(promises).then(e => setLoading(false)).catch(e => setLoading(false));

        } catch (e) {
            console.log(e)
        }
    }, [])

    const handleChangeFirm = (e) => {
        const value = e.target.value;

        setModel(null);
        setFirm(value);
    }

    const handleChangeSelectedCar = (e, id) => {
        setCurrentCar(id);
        setModal(true);
    }

    const handleChangeSelectedTestdrive = (e, id) => {
        setCurrentCar(id);
        setModalTest(true);
    }

    const filterCars = () => {
        let carsTemp = cars;

        if (firm !== "Оберіть виробника")
            carsTemp = carsTemp.filter(x => x.firm === firm);
        if (model)
            carsTemp = carsTemp.filter(x => x.model === model);
        if (category !== "Оберіть тип кузову")
            carsTemp = carsTemp.filter(x => x.car_type === category);
        if (engineType !== "Оберіть тип двигуна")
            carsTemp = carsTemp.filter(x => x.engine === engineType);

        carsTemp = carsTemp.filter(x => (x.engine_volume >= engineRange[0] && x.engine_volume <= engineRange[1]) || !x.engine_volume);
        carsTemp = carsTemp.filter(x => (x.produce_year >= yearRange[0] && x.produce_year <= yearRange[1]) || !x.produce_year);
        carsTemp = carsTemp.filter(x => (x.horse_powers >= enginePRange[0] && x.horse_powers <= enginePRange[1]) || !x.horse_powers);

        return carsTemp;
    }

    return (
        <Box>
            {loading ? <CircularProgress/> :
                <Box display={"flex"} marginTop={"10px"} justifyContent={"space-between"}>
                    {currentCar !== -1 && <ModalCar car={cars.filter(x=>x.id === currentCar)[0]} open={modal} setModal={setModal}></ModalCar>}
                    {currentCar !== -1 && <ModalTestDrive carId={cars.filter(x=>x.id === currentCar)[0].id} open={modalTest} setModal={setModalTest}></ModalTestDrive>}
                    <Box width={"25%"} sx={{background: "rgba(238,238,238,0.46)", padding: "2%"}}>
                        <Typography fontSize={"20px"} sx={{marginBottom: "20px"}}>
                            Сортувати за фільтрами
                        </Typography>
                        <FormControl fullWidth sx={{marginBottom: "40px"}}>
                            <InputLabel id="demo-simple-select-label">Виробник</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={firm}
                                label="Виробник"
                                onChange={handleChangeFirm}
                            >
                                {firms.map((f, i) => (
                                    <MenuItem key={i} value={f}>{f}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <FormControl fullWidth sx={{
                            display: firm !== "Оберіть виробника" ? "inline-flex" : "none",
                            marginBottom: "40px"
                        }}>
                            <InputLabel id="demo-simple-select-label">Модель</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={model}
                                label="Модель"
                                onChange={e => setModel(e.target.value)}
                            >
                                {new Array(...new Set(cars.filter(f => f.firm === firm)))?.map((f, i) => (
                                    <MenuItem key={i} value={f.model}>{f.model}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <FormControl fullWidth sx={{
                            marginBottom: "40px"
                        }}>
                            <InputLabel id="demo-simple-select-label">Тип кузову</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={category}
                                label="Тип кузову"
                                onChange={e => setCategory(e.target.value)}
                            >
                                {categories.map((f, i) => (
                                    <MenuItem key={i} value={f}>{f}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <FormControl fullWidth sx={{
                            marginBottom: "40px"
                        }}>
                            <InputLabel id="demo-simple-select-label">Тип двигуна</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={engineType}
                                label="Тип двигуна"
                                onChange={e => setEngineType(e.target.value)}
                            >
                                {engineTypes.map((f, i) => (
                                    <MenuItem key={i} value={f}>{f}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                        <Slider
                            sx={{marginBottom: "40px"}}
                            getAriaLabel={() => 'Рік випуску'}
                            valueLabelDisplay={"auto"}
                            value={yearRange}
                            onChange={(e, n) => setYearRange(n as number[])}
                            min={2000}
                            max={2022}
                            disableSwap
                            marks={[
                                {
                                    value: 2000,
                                    label: "2000"
                                },
                                {
                                    value: 2022,
                                    label: "2022"
                                },
                            ]}
                        />
                        <Slider
                            sx={{marginBottom: "40px"}}
                            getAriaLabel={() => "Об'єм двигуна"}
                            valueLabelDisplay={"auto"}
                            value={engineRange}
                            onChange={(e, n) => setEngineRange(n as number[])}
                            min={1.0}
                            max={6.0}
                            step={0.1}
                            disableSwap
                            marks={[
                                {
                                    value: 1,
                                    label: "1.0"
                                },
                                {
                                    value: 6,
                                    label: "6.0"
                                },
                            ]}
                        />
                        <Slider
                            sx={{marginBottom: "40px"}}
                            getAriaLabel={() => 'Потужність двигуна'}
                            valueLabelDisplay={"auto"}
                            value={enginePRange}
                            onChange={(e, n) => setEnginePRange(n as number[])}
                            min={100}
                            max={1000}
                            step={10}
                            disableSwap
                            marks={[
                                {
                                    value: 100,
                                    label: "100"
                                },
                                {
                                    value: 1000,
                                    label: "1000"
                                },
                            ]}
                        />
                    </Box>
                    <Box width={"70%"}>
                        <Box display={"flex"} flexWrap={"wrap"}>
                            {filterCars().length > 0 ? filterCars().map(c=>(
                                <Box id={c.id} className={cl.car__card}>
                                    <Box className={cl.content}>
                                        <img width={"50%"}
                                             src={"https://car.ua/wp-content/themes/car-ua/img/main-page/lexus.png"}/>
                                        <Typography className={cl.car__firm}>{c.firm}</Typography>
                                        <Typography className={cl.car__model}>{c.model}</Typography>

                                        <Tooltip title={"Детальніше"}>
                                            <IconButton onClick={e=>handleChangeSelectedCar(e,c.id)} color={"primary"} className={cl.desc}>
                                                <InfoIcon/>
                                            </IconButton>
                                        </Tooltip>
                                        <Tooltip title={"Замовити тестдрайв"}>
                                            <IconButton onClick={e=>handleChangeSelectedTestdrive(e,c.id)} color={"primary"} className={cl.testdrive}>
                                                <DriveEtaIcon/>
                                            </IconButton>
                                        </Tooltip>
                                    </Box>
                                </Box>
                            )) : <Typography fontSize={"32px"} width={"100%"} align={"center"}>Нічого не знайдено!</Typography>}
                        </Box>
                    </Box>
                </Box>
            }
        </Box>
    );
};

export default Catalog;