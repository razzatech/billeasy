'use strict';

angular.module('Merchants')

.controller('MerchantsController',
    ['$scope', '$location', 'MerchantsService',
    function ($scope, $location, MerchantsService) {
		$scope.merchants=[];
		
	    //renew token every 5 seconds
		(function renew_token() {
			MerchantsService.renew_token(function(response) {
				if(response.success) {
					if($location.path().startsWith('/merchants'))
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
		
		//refresh merchants every 5 seconds
		(function refresh_merchants() {
			MerchantsService.fetch_merchants(function(response) {
				if(response.success && $location.path().startsWith('/merchants'))
				{
					
					//remember which merchants where checked
					var checked=[];
					for(var i=0;i<$scope.merchants.length;i++)
					{
						if($scope.merchants[i].checked) {
							checked.push($scope.merchants[i].bill_id);
						}
					}

					$scope.merchants=response.merchants;

					//check them again after updating
					for(var i=0;i<checked.length;i++)
					{
						for(var j=0;j<$scope.merchants.length;j++)
						{
							if(checked[i]==$scope.merchants[j].bill_id) {
								$scope.merchants[j].checked = true;
							}
						}
					}

					console.log("Merchants updated.");
					
					setTimeout(function()
					{
						refresh_merchants();
					}, 5000);
				}
			});
		})();
		
		
		//submit button for new merchant
		$scope.add_merchant = function () {
            $scope.dataLoading = true;

            AdminService.add_merchant($scope.merchant_code, $scope.short_name, $scope.full_name, $scope.contact_person, $scope.contact_number, $scope.address, $scope.email, function(response) {
                if(response.success) {
                    console.log("New merchant " + $scope.short_name + " added.");

                    $location.path('/admin/merchants');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };
		
		//show edit and delete buttons (only) when hovered
		$scope.row_hovered=null;
		
		$scope.row_mouseover = function(index) {
			$scope.row_hovered=index;
		}
		
		$scope.table_mouseleave = function() {
			$scope.row_hovered=null;
		}
		
		$scope.show_row_buttons = function(index) {
			if($scope.row_hovered==index)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		
		
		//"Add merchant" link
		$scope.goto_add_merchant = function() {
			$location.path('/new_merchant');
		}
		
		//"Logout" link
		$scope.logout = function() {
			localStorage.clear();
			console.log("User logged out.");
			$location.path('/');			
		}
    }]);