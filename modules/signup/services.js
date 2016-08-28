'use strict';

angular.module('SignUp')

.factory('SignUpService',
    ['$http', '$cookieStore', '$rootScope', '$timeout',
    function ($http, $cookieStore, $rootScope, $timeout) {
        var service = {};

        service.SignUp = function (given_name, middle_name, surname, address, contact_number, email, user_name, password, callback) {

            var POST_data = {
                given_name:given_name,
                middle_name:middle_name,
                surname:surname,
                address:address,
                contact_number:contact_number,
                email:email,
                user_name:user_name,
                password:password
            }

            $http.post('http://billeasy.razzatech.com/api/_.py/sign_up', POST_data, {headers : {'Content-Type': 'x-www-form-urlencoded'}})
            .success(function (response) {
                    callback(response);
            });
        };

        return service;
    }])

