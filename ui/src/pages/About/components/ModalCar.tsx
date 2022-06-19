import React from 'react';
import {GetCars} from "../../../api/Api";
import {Box, Modal, Paper, Table, TableBody, TableCell, TableContainer, TableRow} from "@mui/material";

const ModalCar = ({car, open, setModal}) => {

    const style = {
        position: 'absolute' as 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        pt: 2,
        px: 4,
        pb: 3,
        borderRadius: "10px"
    };

    return (
        <Modal
            open={open}
            onClose={e => setModal(false)}
            aria-labelledby="parent-modal-title"
            aria-describedby="parent-modal-description"
        >
            <Box sx={{
                ...style,
                minHeight: "600px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "flex-start",
                width: 800
            }}>
                <h2 id="parent-modal-title">Опис авто #{car.id}</h2>
                <img src={car.image} width={"50%"}/>
                <TableContainer component={Paper}>
                    <Table sx={{maxHeight:"500px", overflowY:"auto"}}>
                        <TableBody>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Виробник</TableCell><TableCell>{car.firm}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Модель</TableCell><TableCell>{car.model}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Ємність батереї</TableCell><TableCell>{car.battery_capacity ?? "Відсутня"}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Тип кузову</TableCell><TableCell>{car.car_type}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Тип двигуну</TableCell><TableCell>{car.engine}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Ємність двигуна</TableCell><TableCell>{car.engine_volume ?? "Немає інформації"}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Лошадині сили</TableCell><TableCell>{car.horse_powers}</TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell width={"20%"} sx={{borderRight:"1px solid"}}>Комлпектація</TableCell><TableCell>{car.equipment}</TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        </Modal>
    );
};

export default ModalCar;