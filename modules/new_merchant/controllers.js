'use strict';

angular.module('NewMerchant')

.controller('NewMerchantController',
    ['$scope', '$rootScope', '$location', 'NewMerchantService',
    function ($scope, $rootScope, $location, NewMerchantService) {
		//renew token every 5 seconds
		(function renew_token() {
			NewMerchantService.renew_token(function(response) {
				if(response.success) {
					if($location.path().startsWith('/new_merchant'))
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
		
        //submit button for new merchant
		$scope.add_merchant = function () {
            $scope.dataLoading = true;

            NewMerchantService.add_merchant($scope.merchant_code, $scope.short_name, $scope.full_name, $scope.contact_person, $scope.contact_number, $scope.address, $scope.email, function(response) {
                if(response.success) {
                    console.log("New merchant " + $scope.short_name + " added.");

                    $location.path('/merchants');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };

		//"Bills" link
        $scope.goto_bills = function() {
			$location.path('/bills');
		}
    }]);