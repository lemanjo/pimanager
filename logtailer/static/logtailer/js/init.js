django.jQuery('#start-button').click(function() {
    LogTailer.startReading();
});

django.jQuery('#stop-button').click(function() {
    LogTailer.stopReading();
});

django.jQuery('#auto-scroll').click(function() {
    LogTailer.changeAutoScroll();
});	

django.jQuery('#filter-select').change(function() {
	LogTailer.customFilter();
});		

django.jQuery('#log-window').html("")
LogTailer.customFilter();