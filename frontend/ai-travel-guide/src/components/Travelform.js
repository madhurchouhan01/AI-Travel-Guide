import React, { useState } from 'react';

const TravelForm = () => {
    const [formData, setFormData] = useState({
        distance: '',
        budget: '',
        duration: '',
    });
    const [response, setResponse] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch('http://127.0.0.1:8000/api/recommend/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            const data = await res.json();
            setResponse(data);
        } catch (error) {
            console.error('Error submitting the form:', error);
        }
    };

    return (
        <div>
            <h1>Plan Your Trip</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Distance (in km):</label>
                    <input
                        type="number"
                        name="distance"
                        value={formData.distance}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Budget:</label>
                    <input
                        type="number"
                        name="budget"
                        value={formData.budget}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Duration (in days):</label>
                    <input
                        type="number"
                        name="duration"
                        value={formData.duration}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
            {response && (
                <div>
                    <h2>Recommendations</h2>
                    <ul>
                        {response.destinations?.map((dest, index) => (
                            <li key={index}>
                                {dest.name} - Distance: {dest.distance} km, Cost: ₹{dest.cost}, Duration: {dest.duration} days
                            </li>
                        ))}
                    </ul>
                    <h3>Packing Checklist</h3>
                    <ul>
                        {response.packing_checklist?.map((item, index) => (
                            <li key={index}>{item}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default TravelForm;
