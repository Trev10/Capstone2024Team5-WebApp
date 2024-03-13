import React, { useState, useEffect } from 'react';
import { Typography, Paper, Box, Button } from '@mui/material';

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const token = localStorage.getItem('jwtToken');

  useEffect(() => {
    fetchNotifications();
  }, []);

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'short', day: '2-digit', hour: '2-digit', minute: '2-digit' };
    return date.toLocaleDateString('en-US', options);
  };

  const fetchNotifications = async () => {
    const response = await fetch('http://127.0.0.1:5000/dashboard/notifications', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      }
    });
    if (response.ok) {
      const responseData = await response.json();
      const { notifications } = responseData.data;
      setNotifications(notifications);
    }
  };

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Notifications
      </Typography>
      {notifications && (
        <Paper elevation={6} sx={{ marginTop: 4, padding: 2 }}>
          <Typography variant="6" gutterBottom>
            Notifications
          </Typography>
          {notifications.map((notification) => (
            <Box key={notification.status_id} sx={{ display: 'flex', justifyContent: 'space-between', mt: 1 }}>
              <Typography>
              {formatDate(notification.status_timestamp)}: {notification.notification} 
              </Typography>
              <Button variant="outlined" color="error" onClick={() => deleteAppointment(appointment.appointment_id)}>
                Delete
              </Button>
            </Box>
          ))}
        </Paper>
      )}
    </div>
  );
};

export default Notifications;