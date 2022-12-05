import { useState, useEffect } from "react"
import React from "react";


const Home = () => {
    const [ieqs, setIeqs] = useState([]);
        
    useEffect(() => {
        getData();
    }, [])


    const getData = async () => {
        const response = await fetch('real_time_IEQ.json');
        const data = await response.json();
        // console.log(data)
        setIeqs(data)
    }

    const reloadPage = () => {
        window.location.reload(false);
    }

    return (
    <main>
        <div className="container col-xxl-8 px-4 py-5">
            <h2 className="text-center">Indoor environmental quality dashborad</h2>
            <h5 className="text-center">Real-time IEQs will be updated every 5 minutes</h5>
            <p className="text-center">Click reload button to get new data</p>
            <div className="d-grid gap-2 col-3 mx-auto py-2">
                <button className="btn btn-primary" type="button" onClick={reloadPage}>Reload this page</button>
            </div>
            {ieqs.map((ieq) => {
                const {room, co2, temp, illumination, label, time} = ieq;
                return (
                    <div className="container-fluid text-center py-4">
                        <div className="row">
                            <div className="col">
                                <h3>{room}</h3>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-sm-4">
                                <div className="card text-center">
                                    <div className="card-header">
                                        <h5 className="card-title">CO2</h5>
                                    </div>
                                    <img src={'./img/' + label.substring(0, 2) + '.png'} className="card-img" alt="visualized CO2"></img>
                                    <div className="card-body">
                                        <h5 className="card-text">{co2}</h5>
                                    </div>
                                </div>
                            </div>
                            <div className="col-sm-4 text-center">
                                <div className="card">
                                    <div className="card-header">
                                        <h5 className="card-title">Temperature</h5>
                                    </div>
                                    <img src={'./img/' + label.substring(2, 4) + '.png'} className="card-img" alt="visualized Temperature"></img>
                                    <div className="card-body">
                                        <h5 className="card-text">{temp}</h5>
                                    </div>
                                </div>
                            </div>
                            <div className="col-sm-4 text-center">
                                <div className="card">
                                    <div className="card-header">
                                        <h5 className="card-title">Illumination</h5>
                                    </div>
                                    <img src={'./img/' + label.substring(4, 6) + '.png'} className="card-img" alt="visualized Illumination"></img>
                                    <div className="card-body">
                                        <h5 className="card-text">{illumination}</h5>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <p className="text-center py-2">
                                Last Updated: {time}
                            </p>
                        </div>
                    </div>
                )
            })}
        </div>
    </main>
    )
}

export default Home