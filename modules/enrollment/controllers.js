'use strict';

angular.module('Enrollment')

.controller('EnrollmentController',
    ['$scope', '$rootScope', '$location', 'EnrollmentService',
    function ($scope, $rootScope, $location, EnrollmentService) {
        $scope.accounts = [];
        $scope.billers = ["Meralco", "Maynilad"]; //this list should be fetched from server
        $scope.biller_name=$scope.billers[0];

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

		$scope.enroll = function () {
            $scope.dataLoading = true;

            EnrollmentService.enroll($scope.biller_name, $scope.account_number, function(response) {
                if(response.success) {
                    $scope.dataLoading = false;
					alert("Account successfully enrolled!");
                    $scope.fetch_accounts();
                }
            });
        };
    }]);