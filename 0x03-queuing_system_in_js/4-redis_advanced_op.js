import pkg from 'redis';

const { createClient, print } = pkg

const client = createClient();

client.connect();

client
    .on("error", (error) => {
        if (error) console.log(`Redis client not connected to the server: ${err}`);
    })
    .on("ready", () => {
        console.log('Redis client connected to the server');
    });

client.hSet("HolbertonSchools", "Portland", 50, print);
client.hSet("HolbertonSchools", "Seattle", 80, print);
client.hSet("HolbertonSchools", "New York", 20, print);
client.hSet("HolbertonSchools", "Bogota", 20, print);
client.hSet("HolbertonSchools", "Cali", 40, print);
client.hSet("HolbertonSchools", "Paris", 2, print);

client.hGetAll("HolbertonSchools", (err, result) => {
    if (err) console.log(err)
    else console.log(result)
})