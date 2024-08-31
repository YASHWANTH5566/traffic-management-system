$(document).ready(function() {
    function fetchTrafficData() {
        $.getJSON('/video_feed', function(data) {
            $('#north-count').text(data.vehicle_count);
            $('#north-signal').text(data.signal);

            $('#east-count').text(data.vehicle_count);
            $('#east-signal').text(data.signal);

            $('#south-count').text(data.vehicle_count);
            $('#south-signal').text(data.signal);

            $('#west-count').text(data.vehicle_count);
            $('#west-signal').text(data.signal);
        });
    }

    // Fetch traffic data every 3 seconds
    setInterval(fetchTrafficData, 3000);
});
