# GTest include code for fetch content over the internet 
include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.14.0
)
FetchContent_MakeAvailable(googletest)
add_library(GTest::GTest INTERFACE IMPORTED)
target_link_libraries(GTest::GTest INTERFACE gtest_main gmock_main)
# End GTest include code

# Testing lib library
add_executable(lib-test lib-test.cc)
target_link_libraries(lib-test
 PRIVATE GTest::GTest lib)
add_test(lib-gtests lib-test)

