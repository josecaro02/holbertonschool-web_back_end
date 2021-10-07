import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const KEY = 'HolbertonSchools';

var dict = new Object();
dict = {
    'Portland': 50, 'Seattle':80, 'New York':20, 'Bogota':20, 'Cali':40, 'Paris':21
}
const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

for(var key in dict){
    client.hset(KEY, key, dict[key], redis.print)
}
client.hgetall(KEY, (err, value) => {
  console.log(value);
});
