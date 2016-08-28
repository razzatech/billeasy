'use strict';

angular.module('Admin')

.controller('AdminController',
    ['$scope', '$location', 'AdminService',
    function ($scope, $location, AdminService) {
		$scope.name=localStorage.getItem("name");
        $scope.bills=[];

	    //renew token every 5 seconds
		(function renew_token()
		{
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

        //refresh bills every 5 seconds
		(function refresh_bills()
		{
			AdminService.fetch_bills(function(response) {
				if(response.success && $location.path().startsWith('/admin'))
				{
					//remember which bills where checked
					var checked=[];
					for(var i=0;i<$scope.bills.length;i++)
					{
						if($scope.bills[i].checked) {
							checked.push($scope.bills[i].bill_id);
						}
					}

					$scope.bills=response.bills;

					//check them again after updating
					for(var i=0;i<checked.length;i++)
					{
						for(var j=0;j<$scope.bills.length;j++)
						{
							if(checked[i]==$scope.bills[j].bill_id) {
								$scope.bills[j].checked = true;
							}
						}
					}

					console.log("Bills updated.");

					setTimeout(function()
					{
						refresh_bills();
					}, 5000);
				}
			});
		})();

        $scope.all_bills = function() {
			$location.path('/admin/all_bills');
		}

		$scope.logout = function() {
			localStorage.clear();
			$location.path('/login');
		}
    }]);