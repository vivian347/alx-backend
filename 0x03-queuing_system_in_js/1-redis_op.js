import redis from 'redis';

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

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, result) => {
        if (err) {
            console.log("Error getting school name:", err);
        } else {
            console.log(result);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
