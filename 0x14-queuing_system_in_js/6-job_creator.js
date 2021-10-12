import kue from 'kue'

var queue = kue.createQueue()

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}



var job = queue.create('push_notification_code', jobData).save( function(err){
   if( !err ) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
  });
  
job.on('failed', () => {
console.log('Notification job failed');
});
