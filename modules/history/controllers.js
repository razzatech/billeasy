'use strict';

angular.module('History')

.controller('HistoryController',
    ['$scope', '$rootScope', '$location', 'HistoryService',
    function ($scope, $rootScope, $location, HistoryService) {
        $scope.bills = [];

       //renew token every 5 seconds
		(function renew_token()
		{
			HistoryService.renew_token(function(response) {
			    if($location.path()=='/history')
				{
    				if(response.success) {

    						localStorage.setItem("token", response.token);
    						console.log("Token renewed.");

    						setTimeout(function()
    						{
    							renew_token();
    						}, 5000);

    				} else {
    					localStorage.clear();
    					$location.path('/login');
    					console.log("Authentication failed. Redirecting to login page.")
    				}
				}
			});
		})();
		
		(function refresh_bills()
		{
			HistoryService.fetch_bills(function(response) {
    			if($location.path()=='/history')
    			{
    				$scope.bills=response.bills;
    				console.log("Bills refreshed.");
					
					//setTimeout(function()
					//{
					//	refresh_bills();
					//}, 10000);
    			}
    		});
		})();
		
		//"Logout" link
		$scope.logout = function() {
			localStorage.clear();
			console.log("User logged out.");
			$location.path('/');			
		}
    }]);