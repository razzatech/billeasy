'use strict';

angular.module('Authentication')

.controller('LoginController',
    ['$scope', '$rootScope', '$location', 'AuthenticationService',
    function ($scope, $rootScope, $location, AuthenticationService) {
        $scope.login = function () {
            $scope.dataLoading = true;

            AuthenticationService.Login($scope.user_name_or_email, $scope.password, function(response) {
                if(response.success) {
                    if(response.admin) {
                        localStorage.setItem("admin", 1);
                        console.log("User " + response.name + " (admin) logged in.");
                    }
                    else {
                        console.log("User " + response.name + " logged in.");
                    }

                    localStorage.setItem("name", response.name);
                    localStorage.setItem("token", response.token);

                    $location.path('/');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };
    }]);