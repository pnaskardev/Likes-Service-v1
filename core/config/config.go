package config

import (
	"fmt"
	"sync"

	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

type Config struct {
	Port int `mapstructure:"app_port"`
}

var (
	config *Config
	once   sync.Once
)

func LoadConfig() (*Config, error) {
	once.Do(func() {
		viper := viper.New()
		// Name of the config file without an extension (Viper will intuit the type
		// from an extension on the actual file)
		viper.SetConfigName("config")
		viper.SetConfigType("env")

		// Add search paths to find the file
		// viper.AddConfigPath("/etc/appname/")
		// viper.AddConfigPath("$HOME/.appname")
		viper.AddConfigPath(".")
		// Tells Viper to use this prefix when reading environment variables
		viper.SetEnvPrefix("APP")
		// Alternatively, we can search for any environment variable prefixed and load
		// them in
		viper.AutomaticEnv()

		// Find and read the config file
		err := viper.ReadInConfig()
		if err != nil {
			panic(fmt.Errorf("fatal error config file: %w", err))
		}
		fmt.Println("Using config:", viper.ConfigFileUsed())
		viper.WatchConfig()

		viper.OnConfigChange(func(e fsnotify.Event) {
			fmt.Println("Config file changed:", e.Name)
			viper.Unmarshal(config)
		})

		config = &Config{}
		err = viper.Unmarshal(config)
	})
	return config, nil

}
