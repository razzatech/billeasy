'use strict';

angular.module('Admin')

.controller('AdminController',
    ['$scope', '$location', 'AdminService',
    function ($scope, $location, AdminService) {
		$scope.name=localStorage.getItem("name");

		$scope.merchants=[];
		
	    //renew token every 5 seconds
		(function renew_token() {
			AdminService.renew_token(function(response) {
				if(response.success) {
					if($location.path().startsWith('/admin'))
					{
						localStorage.setItem("token", response.token);
						console.log("Token renewed.");

						setTimeout(function()
						{
							renew_token();
						}, 5000);
					}
				} else {
					localStorage.clear();
					$location.path('/login');
					console.log("Authentication failed. Redirecting to login page.")
				}
			});
		})();
		
		//"Merchants" link
		$scope.goto_merchants = function() {
			$location.path('/merchants');
		}

		//"Bills" link
        $scope.goto_bills = function() {
			$location.path('/bills');
		}

		//"Logout" link
		$scope.logout = function() {
			localStorage.clear();
			console.log("User logged out.");
			$location.path('/');			
		}
    }]);