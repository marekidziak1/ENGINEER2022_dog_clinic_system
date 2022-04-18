$(function () {
  var min = '2022-04-13T00:00';
  var max = '2022-10-13T00:00';

  // Mobiscroll Calendar initialization
  $('#demo-booking-datetime').mobiscroll().datepicker({
      display: 'inline',                       // Specify display mode like: display: 'bottom' or omit setting to use default
      controls: ['calendar', 'timegrid'],      // More info about controls: https://docs.mobiscroll.com/5-16-0/calendar#opt-controls
      min: min,                                // More info about min: https://docs.mobiscroll.com/5-16-0/calendar#opt-min
      max: max,                                // More info about max: https://docs.mobiscroll.com/5-16-0/calendar#opt-max
      minTime: '08:00',
      maxTime: '19:59',
      stepMinute: 60,
      width: null,                             // More info about width: https://docs.mobiscroll.com/5-16-0/calendar#opt-width
      onPageLoading: function (event, inst) {  // More info about onPageLoading: https://docs.mobiscroll.com/5-16-0/calendar#event-onPageLoading
          getDatetimes(event.firstDay, function callback(bookings) {
              inst.setOptions({
                  labels: bookings.labels,     // More info about labels: https://docs.mobiscroll.com/5-16-0/calendar#opt-labels
                  invalid: bookings.invalid    // More info about invalid: https://docs.mobiscroll.com/5-16-0/calendar#opt-invalid
              });
          });
      }
  });
  function getPrices(d, callback) {
      var invalid = [],
          labels = [];

      mobiscroll.util.http.getJson('https://trial.mobiscroll.com/getprices/?year=' + d.getFullYear() + '&month=' + d.getMonth(), function (bookings) {
          for (var i = 0; i < bookings.length; ++i) {
              var booking = bookings[i],
                  d = new Date(booking.d);

              if (booking.price > 0) {
                  labels.push({
                      start: d,
                      title: '$' + booking.price,
                      textColor: '#e1528f'
                  });
              } else {
                  invalid.push(d);
              }
          }
          callback({ labels: labels, invalid: invalid });
      }, 'jsonp');
  }

  function getDatetimes(day, callback) {
      var invalid = [];
      var labels = [];

      mobiscroll.util.http.getJson('https://trial.mobiscroll.com/getbookingtime/?year=' + day.getFullYear() + '&month=' + day.getMonth(), function (bookings) {
          for (var i = 0; i < bookings.length; ++i) {
              var booking = bookings[i];
              var bDate = new Date(booking.d);

              if (booking.nr > 0) {
                  labels.push({
                      start: bDate,
                      title: booking.nr + ' SPOTS',
                      textColor: '#e1528f'
                  });
                  $.merge(invalid, booking.invalid);
              } else {
                  invalid.push(bDate);
              }
          }
          callback({ labels: labels, invalid: invalid });
      }, 'jsonp');
  }

  function getBookings(d, callback) {
      var invalid = [],
          labels = [];

      mobiscroll.util.http.getJson('https://trial.mobiscroll.com/getbookings/?year=' + d.getFullYear() + '&month=' + d.getMonth(), function (bookings) {
          for (var i = 0; i < bookings.length; ++i) {
              var booking = bookings[i],
                  d = new Date(booking.d);

              if (booking.nr > 0) {
                  labels.push({
                      start: d,
                      title: booking.nr + ' SPOTS',
                      textColor: '#e1528f'
                  });
              } else {
                  invalid.push(d);
              }
          }
          callback({ labels: labels, invalid: invalid });
      }, 'jsonp');
  }
});