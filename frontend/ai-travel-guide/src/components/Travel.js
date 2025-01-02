import React, { useState } from 'react';
import { useAuth0 } from "@auth0/auth0-react";

const TravelForm = () => {
  const {user} = useAuth0();
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
    console.log(formData)
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch('http://127.0.0.1:8000/api/recommend/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  ...formData,
                  user : user
                }),
            });
            const data = await res.json();
            setResponse(data);
            console.log('Data sent to backend:', data); 
        } catch (error) {
            console.error('Error submitting the form:', error);
        }
    };

    return (
        <div>
            <span className='flow-root'>
                <h1 className='text-4xl'>Plan Your Trip!!!</h1>
             </span>
            
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Distance (in km):</label><br/>
                    <input
                        className='border-2 border-sky-500'
                        type="number"
                        name="distance"
                        value={formData.distance}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Budget:</label><br/>
                    <input
                        className='border-2 border-sky-500'
                        type="number"
                        name="budget"
                        value={formData.budget}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Duration (in days):</label><br/>
                    <input
                        className='border-2 border-sky-500'
                        type="number"
                        name="duration"
                        value={formData.duration}
                        onChange={handleChange}
                        required
                    />
                </div>
                
                <button className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2" type="submit">Submit</button>
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

