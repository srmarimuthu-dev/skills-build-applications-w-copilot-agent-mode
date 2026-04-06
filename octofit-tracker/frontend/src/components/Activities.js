import React, { useState } from 'react';

const Activities = () => {
  const [activityType, setActivityType] = useState('');
  const [duration, setDuration] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle activity logging
    console.log('Activity:', activityType, duration);
  };

  return (
    <div className="container mt-5">
      <h2>Log Activity</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Activity Type</label>
          <input
            type="text"
            className="form-control"
            value={activityType}
            onChange={(e) => setActivityType(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Duration (minutes)</label>
          <input
            type="number"
            className="form-control"
            value={duration}
            onChange={(e) => setDuration(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">Log Activity</button>
      </form>
    </div>
  );
};

export default Activities;