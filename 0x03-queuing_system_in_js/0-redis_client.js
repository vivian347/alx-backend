import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

redisClient.connect();

redisClient.disconnect();