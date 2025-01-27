import React, { useState, useEffect } from 'react';
import { useAuth0 } from "@auth0/auth0-react";
import './Travel.css';
import Button from './Submit';
import './Cards.css'

const TravelForm = () => {
    const [latitude, setLatitude] = useState(null);
    const [longitude, setLongitude] = useState(null);
    const [loading, setLoading] = useState(false);
    const [response, setResponse] = useState(null);
    const [moveUp, setMoveUp] = useState(false); // Added state for moving the form up

    const { user } = useAuth0();

    const [formData, setFormData] = useState({
        distance: '',
        budget: '',
        duration: '',
    });

    useEffect(() => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    setLatitude(position.coords.latitude);
                    setLongitude(position.coords.longitude);
                },
                (error) => {
                    console.error("Error fetching location:", error.message);
                }
            );
        } else {
            console.error("Geolocation is not supported by this browser.");
        }
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await fetch('http://127.0.0.1:8000/api/recommend/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    ...formData,
                    user: user,
                    latitude,
                    longitude,
                }),
            });
            const data = await res.json();
            setResponse(data);
            setMoveUp(true); // Trigger the animation to move the form up
        } catch (error) {
            console.error('Error submitting the form:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <div className={`form-container ${moveUp ? 'move-up' : ''}`}>
                <div className='form'>
                    <h1>Plan Your Trip</h1>
                    <form onSubmit={handleSubmit}>
                        <div>
                            <label className='label'>Distance (in km)</label><br />
                            <input
                                className='box'
                                type="number"
                                name="distance"
                                value={formData.distance}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <div>
                            <label className='label'>Budget</label><br />
                            <input
                                className='box'
                                type="number"
                                name="budget"
                                value={formData.budget}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <div>
                            <label className='label'>Duration (in days)</label><br />
                            <input
                                className='box'
                                type="number"
                                name="duration"
                                value={formData.duration}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        <button type="submit" disabled={loading}>
                            {loading ? "Loading..." : <Button />}
                        </button>
                    </form>
                </div>

                {loading && (
                    <div className="loading">
                        <div className="spinner"></div>
                        <p>Fetching recommendations...</p>
                    </div>
                )}

                {!loading && response && (
                    <div className="response">
                        <h1 className='response-recom'>Recommendations</h1>
                        <div className='cards-container'>
                            {response.destinations?.map((dest, index) => (
                                <div className='card' key={index}>
                                    <h2>{dest.name}</h2>
                                    <p><strong>Address:</strong> {dest.address} km</p>
                                    <p><strong>Cost:</strong> {dest.categories[0] === 12103 ? "Free" : "₹00.00"}</p>
                                    <p><strong>Duration:</strong> {dest.duration} days</p>
                                    <p>Find more places</p>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

            </div>
        </>

    );
};

export default TravelForm;

{/* <h3>Packing Checklist</h3>
<ul>
    {response.packing_checklist?.map((item, index) => (
        <li key={index}>{item}</li>
    ))}
</ul> */}