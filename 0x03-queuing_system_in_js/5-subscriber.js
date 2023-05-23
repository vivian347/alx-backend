import redis from "redis";

const client = redis.createClient();

client.connect();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (error) => {
    console.log("Redis client not connected to the server:", error);
});

(async () => {
    // const subscriber = client.duplicate();
    // await subscriber.connect();
    await client.subscribe('holberton school channel', (message) => {
        console.log(message);
        if (message === "KILL_SERVER") {
            client.unsubscribe(channel);
            process.exit(0);
        }
    })
})

// client.subscribe('holberton school channel');

// client.on("message", (channel, message) => {
//     console.log(message);

//     if (message === "KILL_SERVER") {
//         client.unsubscribe(channel);
//         process.exit(0)
//     }
// })
