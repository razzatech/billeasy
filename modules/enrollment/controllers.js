'use strict';

angular.module('Enrollment')

.controller('EnrollmentController',
    ['$scope', '$rootScope', '$location', 'EnrollmentService',
    function ($scope, $rootScope, $location, EnrollmentService) {
        $scope.accounts = [];
        $scope.merchants;
        $scope.selected_merchant;

        //fetch accounts
        $scope.fetch_accounts = function () {
            EnrollmentService.fetch_accounts(function(response) {
    			if($location.path()=='/enrollment')
    			{
    				$scope.accounts=response.accounts;

    				console.log("Accounts retrieved.");
    			}
    		});
        }
        $scope.fetch_accounts();
		
        //renew token every 5 seconds
		(function renew_token()
		{
			EnrollmentService.renew_token(function(response) {
			    if($location.path()=='/enrollment')
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
		
		//fetch merchants for select box
		(function refresh_merchants() {
			EnrollmentService.fetch_merchants(function(response) {
				if(response.success)
				{
					$scope.merchants=response.merchants;
					$scope.selected_merchant=$scope.merchants[0];
					console.log("Merchants updated.");
				}
			});
		})();
	
		//enroll new account
		$scope.enroll = function () {
            $scope.dataLoading = true;

            EnrollmentService.enroll($scope.selected_merchant.merchant_code, $scope.account_number, $scope.custom_name, function(response) {
                if(response.success) {
                    $scope.dataLoading = false;
					alert("Account successfully enrolled!");
                    $scope.fetch_accounts();
                }
            });
        };
		
		//"Logout" link
		$scope.logout = function() {
			localStorage.clear();
			console.log("User logged out.");
			$location.path('/');			
		}
    }]);