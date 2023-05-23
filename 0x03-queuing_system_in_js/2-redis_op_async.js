import redis from "redis";

const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (error) => {
    console.log("Redis client not connected to the server:", error);
});

client.connect();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {

        redis.print(`Reply: ${reply}`);

    });
}

async function displaySchoolValue(schoolName) {
    const reply = await client.get(schoolName);
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');