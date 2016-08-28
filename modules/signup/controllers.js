'use strict';

angular.module('SignUp')

.controller('SignUpController',
    ['$scope', '$rootScope', '$location', 'SignUpService',
    function ($scope, $rootScope, $location, SignUpService) {
        $scope.login = function () {
            $scope.dataLoading = true;

            SignUpService.SignUp($scope.given_name, $scope.middle_name, $scope.surname, $scope.address, $scope.contact_number, $scope.email, $scope.username, $scope.password, function(response) {
                if(response.success) {
                    console.log("New user " + response.name + " logged in.");

                    localStorage.setItem("name", response.name);
                    localStorage.setItem("token", response.token);
                    $location.path('/#/home');
                } else {
                    $scope.error = response.message;
                    $scope.dataLoading = false;
                }
            });
        };
    }]);